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
%Runs = {'Run3', 'Run5', 'Run6', 'Run7', 'Run8'}; %Eps dependance
Runs = {'Run3', 'Run11', 'Run12'}; %Actuator points dependance
Power_avg = [];
CP_avg = [];

%% Processing all the Runs
for k = 1:size(Runs,2)
    %% Reading the data
    Folder = '/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/';
    Subfolder = Runs{k};
    File = '/Results/turbineOutput/0/powerRotor';
    Path = strcat(Folder, Subfolder, File);
    Vars_preserve = {'Turbine', 'Time_s_', 'rotorPower_W_'};
    Disp_vars = false;
    Data = ReadCSV(Path, Vars_preserve, Disp_vars);

    %% Extracting the power generation at the rotor
    Power_rotor = [];
    j = 1;
    for i = 1:size(Data,1)
        if Data(i,1) == 1
            Power_rotor(j,:) = Data(i,:);
            j = j+1;
        end
    end

    %% Plotting the change in power with time
    fgc = fgc+1;
    figure(fgc)
    plot(Power_rotor(:,2), Power_rotor(:,3));
    hold on
    grid on
    xlabel('Time [s]')
    ylabel('Power [W]')
    title(sprintf('Power generation - %s', Runs{k}))
    set(gca,FS,14)

    %% Averaging the power generation
    ti = 5;
    dt = 7e-4;
    ti_index = round(ti/dt + 1);
    sum = 0;
    n = size(Power_rotor,1);
    for i = ti_index:n
        sum = sum + Power_rotor(i,3);
    end
    Power_avg(k) = sum/(n-ti_index);

    %% Computing CP
    CP_avg(k) = Power_avg(k)/Power_wind;

end

