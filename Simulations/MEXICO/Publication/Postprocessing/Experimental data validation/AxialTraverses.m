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

%% Runs to analyze
Runs = {'Run14', 'Run17', 'Run18'}; %V10, V15, V24 m/s results

%% Tower location
y_tower = 0:0.1:1.5;
x_tower = 0*y_tower;

%% Reading experimental data
%Axial traverses
AT_exp_path = 'ExperimentalData/AxialTraverses/AxialTraverses.csv';
Vars = {'V10_X','V10_Y','V15_X','V15_Y','V24_X','V24_Y'};
AT_exp_mat = ReadCSV(AT_exp_path, Vars, false);
j = 1;
for i = 1:2:size(Vars,2)
    AT_exp{j} = AT_exp_mat(:,i:i+1);
    j = j+1;
end
clear AT_exp_path AT_exp_mat Vars

%% Plotting the rotor location
AT_plot = figure();
tower_color = '#ACACAC';
plot(x_tower, y_tower, LW, 1, C, tower_color, 'HandleVisibility','off');
hold on

%% Plotting the experimental results
%Axial traverses
figure(AT_plot)
bullets = {'ok', 'sk', '^k'};
plot(AT_exp{1}(:,1), AT_exp{1}(:,2), bullets{1}, MS, 4); hold on
plot(AT_exp{2}(:,1), AT_exp{2}(:,2), bullets{2}, MS, 4); hold on
plot(AT_exp{3}(:,1), AT_exp{3}(:,2), bullets{3}, MS, 4); hold on


%% Analyzing the axial traverses
Folder = '/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/';
Subfolder = '/Postprocessing/AT/';
AT = {'AT1', 'AT2', 'AT3'};
LS_array = {'-'; '--'; '-.'};
for i = 1:size(Runs,2)
    %Reading the data
    for j = 1:size(AT,2)
        PATH = strcat(Folder, Runs{i}, Subfolder, AT{j}, '.csv');
        Vars = {'Points_0', 'UMean_0'};
        Data{j} = ReadCSV(PATH, Vars, false);
    end
    %Averaging the readings
    AT_num(:,1) = Data{1}(:,1);
    for k = 1:size(AT_num,1)
        sum = 0;
        for j = 1:size(Runs,2)
            sum = sum + Data{j}(k,2);
        end
        AT_num(k,2) = sum/3;
    end
    %Extracting the reference velocity
    Uref(i) = AT_num(1,2);
    %Normalizing the data
    AT_num(:,1) = (AT_num(:,1)-15)./4.5;
    AT_num(:,2) = AT_num(:,2)./Uref(i);
    %Plotting the velocity profile
    figure(AT_plot)
    plot(AT_num(:,1), AT_num(:,2), LS_array{i}, LW, 1.5, C, 'k')
    hold on
    
    %Computing the MSE
    n = size(AT_exp{i},1);
    dx = abs(AT_num(1,1) - AT_num(2,1));
    sum = 0;
    for j = 1:n
        index = round(((AT_exp{i}(j,1)-AT_num(1,1))/dx)+1);
        if index < 0
            index = 1;
        elseif index > size(AT_num,1)
            index = size(AT_num,1);
        end
        diff = (AT_exp{i}(j,2) - AT_num(index,2))^2;
        sum = sum + diff;
    end
    MSE(i) = 1/n*sum;
end
MSE = MSE';

%% Labeling the AT plot
figure(AT_plot);
lgd = legend('$U_{in} = 10 \ m/s$', ... 
             '$U_{in} = 15 \ m/s$', ...
             '$U_{in} = 24 \ m/s$', ...
             '$U_{in} = 10 \ m/s$', ...
             '$U_{in} = 15 \ m/s$', ...
             '$U_{in} = 24 \ m/s$');
set(lgd, 'Interpreter', 'latex')
set(lgd, 'Location', 'southwest') 
xmin = -1;
xmax = 1.32;
dx_ticks = 0.5;
xlim([xmin,xmax])
xticks(xmin:dx_ticks:xmax)
ymin = 0;
ymax = 1.05;
dy_ticks = 0.2;
ylim([ymin, ymax])
yticks(ymin:dy_ticks:ymax)
axis = gca;
axis.XAxis.MinorTick = 'on';
axis.YAxis.MinorTick = 'on';
ylabel('$a = U/U_{ref}$')
xlabel('$x/D$')
% order = get(axis, 'Children');
% set(axis, 'Children', flipud(order))
title_text = 'Axial induction - $t: 5-15s$ - $r/R = 0.82$ - $1.5$M cells - $\varepsilon_R = 0.2$ - $\varepsilon_T = 0.1$';
title(title_text, 'Interpreter', 'latex')

%% Saving the AT plot
figure(AT_plot)
set(gcf, 'Units', 'inches', 'Position', [5, 5, 5.6, 3.6], 'PaperSize', [5.7,3.7])
saveas(AT_plot, 'Axial traverses', 'png');

