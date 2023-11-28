function [] = Anonimize(dataFolder)

files = dir(dataFolder);
files = files(3:end); % first two are . and ..
dirFlags = [files.isdir];
subFolders = files(dirFlags);

caseFolderOutput = strcat(dataFolder,'_anon');
mkdir(caseFolderOutput);

% Read all subfolders
for iS = 1:length(subFolders)
    
    fprintf('Anonimizing data : %s...\n',fullfile(subFolders(iS).folder,subFolders(iS).name));
    files = dir(fullfile(subFolders(iS).folder,subFolders(iS).name));
    files = files(3:end);
    
    subFolderOutput = strcat(caseFolderOutput,'/',subFolders(iS).name);
    mkdir(subFolderOutput);
    
    % Read all files
    for iF= 1:length(files)
        
        im = dicomread(fullfile(subFolders(iS).folder,subFolders(iS).name,files(iF).name));
        dicomInfo = dicominfo(fullfile(subFolders(iS).folder,subFolders(iS).name,files(iF).name));
        
        %% Anonimize the data
        dicomInfo.PatientName = '';
        dicomInfo.PatientBirthDate = '';
        dicomInfo.PatientAddress = '';
        dicomInfo.PatientIdentityRemoved = 'YES';
        dicomInfo.PatientID = '';
        dicomInfo.OtherPatientID = '';
        
        %% Write anonimized data
        dicomwrite(im,fullfile(subFolderOutput,files(iF).name),dicomInfo);
        
    end
    
end

end

