function [] = Anonimize(dataFolder)
% 
% files = dir(dataFolder);
% files = files(3:end); % first two are . and ..
% dirFlags = [files.isdir];
% subFolders = files(dirFlags);

% dirinfo = dir(dataFolder);
% dirinfo(~[dirinfo.isdir]) = [];  %remove non-directories
% 
% subdirinfo = cell(length(dirinfo));
% for K = 1 : length(dirinfo)
%   thisdir = dirinfo(K).name;
%   subdirinfo{K} = dir(fullfile(thisdir, '*.dcm'));
% end

path = uigetdir(dataFolder);
files = dir(fullfile(path,'**','*.dcm'));
nFiles = length(files);

for f = 1:nFiles
    fprintf('Anonimizing data : %s...\n',fullfile(files(f).folder,files(f).name));
    
    im = dicomread(fullfile(files(f).folder,files(f).name));
    dicomInfo = dicominfo(fullfile(files(f).folder,files(f).name));
    
    %% Anonimize the data
    dicomInfo.PatientName = '';
    dicomInfo.PatientBirthDate = '';
    dicomInfo.PatientAddress = '';
    dicomInfo.PatientIdentityRemoved = 'YES';
    dicomInfo.PatientID = '';
    dicomInfo.OtherPatientID = '';
    
    %% Write anonimized data
    dicomwrite(im,fullfile(files(f).folder,files(f).name),dicomInfo);
end

% 
% caseFolderOutput = strcat(dataFolder,'_anon');
% mkdir(caseFolderOutput);
% 
% % Read all subfolders
% for iS = 1:length(subFolders)
%     
%     fprintf('Anonimizing data : %s...\n',fullfile(subFolders(iS).folder,subFolders(iS).name));
%     files = dir(fullfile(subFolders(iS).folder,subFolders(iS).name));
%     files = files(3:end);
%     
%     subFolderOutput = strcat(caseFolderOutput,'/',subFolders(iS).name);
%     mkdir(subFolderOutput);
% 
%     dirFlags = [files.isdir];
%     subFolders2 = files(dirFlags);
%     
% %     for iS2 = 1:length(subFolders2)
% %         fprintf('Anonimizing data : %s...\n',fullfile(subFolders(iS).folder,subFolders(iS).name));
% %         files = dir(fullfile(subFolders(iS).folder,subFolders(iS).name));
% %         files = files(3:end);
% %         
% %         subFolderOutput = strcat(caseFolderOutput,'/',subFolders(iS).name);
% %         mkdir(subFolderOutput);
%         
%         
%     % Read all files
%     for iF= 1:length(files)
%         
%         im = dicomread(fullfile(subFolders(iS).folder,subFolders(iS).name,files(iF).name));
%         dicomInfo = dicominfo(fullfile(subFolders(iS).folder,subFolders(iS).name,files(iF).name));
%         
%         %% Anonimize the data
%         dicomInfo.PatientName = '';
%         dicomInfo.PatientBirthDate = '';
%         dicomInfo.PatientAddress = '';
%         dicomInfo.PatientIdentityRemoved = 'YES';
%         dicomInfo.PatientID = '';
%         dicomInfo.OtherPatientID = '';
%         
%         %% Write anonimized data
%         dicomwrite(im,fullfile(subFolderOutput,files(iF).name),dicomInfo);
%         
%     end
%     
% end

end

