clc
clear all
close all

MRI_dataset = '/data/Dropbox/imaging_data/2019022801EP/MR';

mkdir(strcat(MRI_dataset,'_anon'));

cmd = ['cp -r ',strcat(MRI_dataset,'/*'),' ',strcat(MRI_dataset,'_anon')];
system(cmd);

% Anonimize_CT(strcat(MRI_dataset,'_anon')); 
Anonimize(strcat(MRI_dataset,'_anon')); 