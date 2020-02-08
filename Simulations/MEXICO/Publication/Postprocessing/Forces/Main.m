clc
clear all
close all

%Global variables
FS = 'FontSize';
LW = 'LineWidth';
fgc = 0; %Figure count

%% Computing the power available in the wind
rho = 1.225; %kg/m^3
U_in = 10; %m/s
D = 4.5; %m
A = pi/4*D^2; %m^2
Power_wind = 1/2*rho*A*U_in^3;

%% Listing all the Runs to analyze
%Runs = {'Run1', 'Run2', 'Run3', 'Run4'}; %Mesh dependance
%Runs = {'Run3', 'Run5', 'Run6', 'Run7', 'Run8', 'Run9', 'Run10'}; %Rotor Eps dependance
%Runs = {'Run3', 'Run11', 'Run12'}; %Actuator points dependance
Runs = {'Run14', 'Run15', 'Run16'}; %Tower Eps dependance
Thrust_tower_avg = [];
Thrust_rotor_avg = [];
Thrust_total_avg = [];

%% Processing all the Runs
for k = 1:size(Runs,2)
    %% Reading the data
    Folder = '/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/';
    Subfolder = Runs{k};
    File = '/Results/turbineOutput/0/thrust';
    Path = strcat(Folder, Subfolder, File);
    Vars_preserve = {'Turbine', 'Time_s_', 'thrust_N_'};
    Disp_vars = false;
    Data = ReadCSV(Path, Vars_preserve, Disp_vars);
    
    %% Extracting the thrust for both the tower and the rotor
    Thrust_tower = [];
    j = 1;
    for i=1:2:size(Data,1)
        Thrust_tower(j,:) = Data(i,2:3);
        j = j+1;
    end
    
    Thrust_rotor = [];
    j = 1;
    for i=2:2:size(Data,1)
        Thrust_rotor(j,:) = Data(i,2:3);
        j = j+1;
    end 
        
    %% Plotting the change in thrust with time
    fgc = fgc+1;
    figure(fgc)
    plot(Thrust_tower(:,1), Thrust_tower(:,2), LW, 2);
    hold on
    grid on
    xlabel('Time [s]')
    ylabel('Thrust [N]')
    title(sprintf('Thrust in the tower - %s', Runs{k}))
    set(gca,FS,14)
    
    %% Plotting the change in thrust with time
    fgc = fgc+1;
    figure(fgc)
    plot(Thrust_rotor(:,1), Thrust_rotor(:,2));
    hold on
    grid on
    xlabel('Time [s]')
    ylabel('Thrust [N]')
    title(sprintf('Thrust in the rotor - %s', Runs{k}))
    set(gca,FS,14)

    %% Averaging the thrust
    ti = 5;
    dt = 7e-4;
    ti_index = round(ti/dt + 1);
    sum_tower = 0;
    sum_rotor = 0;
    n = size(Thrust_rotor,1);
    for i = ti_index:n
        sum_tower = sum_tower + Thrust_tower(i,2);
        sum_rotor = sum_rotor + Thrust_rotor(i,2);
    end
    Thrust_tower_avg(k) = sum_tower/(n-ti_index);
    Thrust_rotor_avg(k) = sum_rotor/(n-ti_index);
    Thrust_total_avg(k) = Thrust_tower_avg(k) + Thrust_rotor_avg(k);
end

Thrust_tower_avg = Thrust_tower_avg';
Thrust_rotor_avg = Thrust_rotor_avg';
Thrust_total_avg = Thrust_total_avg';
