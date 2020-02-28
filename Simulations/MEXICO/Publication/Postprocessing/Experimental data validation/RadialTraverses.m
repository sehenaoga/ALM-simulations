clc
clear all
close all

%Global variables
FS = 'FontSize';
LW = 'LineWidth';
LS = 'LineStyle';
C = 'Color';
MFC = 'MarkerFaceColor';
MEC = 'MarkerEdgeColor';
MS = 'MarkerSize';
set(0,'defaultTextInterpreter','latex');

%% Runs to analyze and its reference velocities
Runs = {'Run14', 'Run17', 'Run18'}; %V10, V15, V24 m/s results
Uref = [9.6573   14.6973   23.8163];

%% Rotor location
Rotor_0 = [15, 11.25, 5];
y_rotor = 0:0.1:1.5;
x_rotor = 0*y_rotor;

Tower_0 = (18-15)/4.5; %Upwind
%Tower_0 = (12-15)/4.5; %Downwind

%% Reading experimental data
%Radial traverses
RT_exp_path = 'ExperimentalData/RadialTraverses/';
Vels = {'V10', 'V15', 'V24'};
V = [10, 15, 24];
Vars = {'z_D_0_56_X','z_D_0_56_Y','z_D_0_36_X','z_D_0_36_Y','z_D0_34_X','z_D0_34_Y','z_D1_04_X','z_D1_04_Y'};
for i = 1:size(Vels,2)
    RT_PATH = strcat(RT_exp_path, Vels{i}, '/', Vels{i}, '.csv');
    RT_exp{i} = ReadCSV(RT_PATH, Vars, false);
end
j = 1;
for i = 1:2:size(Vars,2)
    RT_exp_V10{j} = RT_exp{1}(:,i:i+1);
    j = j+1;
end
j = 1;
for i = 1:2:size(Vars,2)
    RT_exp_V15{j} = RT_exp{2}(:,i:i+1);
    j = j+1;
end
j = 1;
for i = 1:2:size(Vars,2)
    RT_exp_V24{j} = RT_exp{3}(:,i:i+1);
    j = j+1;
end
clear RT_exp_path Vels Vars RT_exp RT_PATH

%% Plotting the experimental results
bullets = {'ok', 'sk', 'dk', '+k'};
%Radial traverses - V10
RT_V10_plot = figure();
for i = 1:size(RT_exp_V10,2)
    plot(RT_exp_V10{i}(:,1), RT_exp_V10{i}(:,2), bullets{i}, MS, 4); hold on
end
%Radial traverses - V15
RT_V15_plot = figure();
for i = 1:size(RT_exp_V15,2)
    plot(RT_exp_V15{i}(:,1), RT_exp_V15{i}(:,2), bullets{i}, MS, 4); hold on
end
%Radial traverses - V24
RT_V24_plot = figure();
for i = 1:size(RT_exp_V24,2)
    plot(RT_exp_V24{i}(:,1), RT_exp_V24{i}(:,2), bullets{i}, MS, 4); hold on
end
plots = [RT_V10_plot, RT_V15_plot, RT_V24_plot];

%% Analyzing the radial traverses
Folder = '/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/';
Subfolder = '/Postprocessing/RT/';
RT = {'RT1-', 'RT2-', 'RT3-', 'RT4-'};
LS_array = {'-'; '--'; '-.'; ':'};
RT_n = 3; %Number of extracted profiles
for i = 1:size(Runs,2)
    RT_num = {};
    for j = 1:size(RT,2)
        %Reading the data
        for k = 1:RT_n
            PATH = strcat(Folder, Runs{i}, Subfolder, RT{j}, int2str(k), '.csv');
            Vars = {'Points_2', 'UMean_0'};
            Data{k} = ReadCSV(PATH, Vars, false);            
        end
        %Averaging the readings
        RT_num{j}(:,1) = Data{1}(:,1);
        for k = 1:size(RT_num{j},1)
            sum = 0;
            for m = 1:size(RT_n,2)
                sum = sum + Data{m}(k,2);
            end
            RT_num{j}(k,2) = sum/size(RT_n,2);
        end
        %Normalizing the data
        RT_num{j}(:,1) = (RT_num{j}(:,1)-Rotor_0(3))./(4.5/2);
        RT_num{j}(:,2) = RT_num{j}(:,2)./Uref(i);
        %Plotting the velocity profile
        figure(plots(i))
        plot(RT_num{j}(:,2), RT_num{j}(:,1), LS_array{j}, LW, 1.5, C, 'k')
        hold on
    end
end

%% Labeling the RT plots
for i = 1:size(plots,2)
    figure(plots(i));
    lgd = legend('$x/D = -0.56$', ... 
                 '$x/D = -0.36$', ...
                 '$x/D = 0.34$', ...
                 '$x/D = 1.04$', ...
                 '$x/D = -0.56$', ... 
                 '$x/D = -0.36$', ...
                 '$x/D = 0.34$', ...
                 '$x/D = 1.04$');
    set(lgd, 'Interpreter', 'latex', FS, 6)
    if (i == 1)
        set(lgd, 'Location', 'southwest')
    else 
        set(lgd, 'Location', 'northwest')
    end
    if (i == 3)
        xmin = 0.6;
        xmax = 1.025;
    else 
        xmin = 0;
        xmax = 1.025;
    end
    dx_ticks = 0.2;
    xlim([xmin,xmax])
    xticks(xmin:dx_ticks:xmax)
    ymin = 0;
    ymax = 1.52;
    dy_ticks = 0.5;
    ylim([ymin, ymax])
    yticks(ymin:dy_ticks:ymax)
    axis = gca;
    axis.XAxis.MinorTick = 'on';
    axis.YAxis.MinorTick = 'on';
    xlabel('$a = U/U_{ref}$')
    ylabel('$r/R$')
    title_text = 'Axial induction - Radial Traverses - $t: 5-15s$ - $1.5$M cells - $\varepsilon_R = 0.2$ - $\varepsilon_T = 0.1$';
    title(title_text, 'Interpreter', 'latex')
end

%% Saving the RT plots
for i = 1:size(plots,2)
    figure(plots(i))
    set(gcf, 'Units', 'inches', 'Position', [5, 5, 5.6, 3.6], 'PaperSize', [5.7,3.7])
    saveas(plots(i), strcat('RadialTraverse-', int2str(i)), 'pdf');
end

