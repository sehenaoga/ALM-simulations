clc
clear all
close all

%Global variables
FS = 'FontSize';
def_FS = 20;
LW = 'LineWidth';
def_LW = 2;
LS = 'LineStyle';
L = 'Location';
C = 'Color';
MFC = 'MarkerFaceColor';
MEC = 'MarkerEdgeColor';
MS = 'MarkerSize';
def_MS = 7;
%Latex interpreters
set(groot,'defaulttextinterpreter','latex');
set(groot, 'defaultAxesTickLabelInterpreter','latex');
set(groot, 'defaultLegendInterpreter','latex');

%% Runs to analyze
Runs = {'Run19', 'Run20', 'Run21'}; %V10, V15, V24 m/s results

%% Rotor location
Rotor_0 = [15, 11.25, 5];
y_rotor = 0:0.1:1.5;
x_rotor = 0*y_rotor;
%Tower location
Tower_0 = (12-15)/4.5; %Downwind
y_tower = 0:0.1:1.5;
x_tower = 0*y_tower+Tower_0;

%% Plotting the rotor location
AT_plot = figure();
rotor_color = '#ACACAC';
plot(x_rotor, y_rotor, '-', LW, 1.5, C, rotor_color, 'HandleVisibility','off');
hold on

%% Plotting the tower location
figure(AT_plot)
tower_color = '#ACACAC';
plot(x_tower, y_tower, '-', LW, 1.5, C, tower_color, 'HandleVisibility','off');
hold on

%% Analyzing the axial traverses
%Folder = '/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/';
Folder = '/Users/Sebastian/Documents/ALM-simulations/Simulations/MEXICO/Publication/';
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
        for j = 1:size(AT,2)
            sum = sum + Data{j}(k,2);
        end
        AT_num(k,2) = sum./size(AT,2);
    end
    %Extracting the reference velocity
    Uref(i) = AT_num(1,2);
    %Normalizing the data
    AT_num(:,1) = (AT_num(:,1)-15)./4.5;
    AT_num(:,2) = AT_num(:,2)./Uref(i);
    %Plotting the velocity profile
    figure(AT_plot)
    plot(AT_num(:,1), AT_num(:,2), LS_array{i}, LW, def_LW, C, 'k')
    hold on
end

%% Labeling the AT plot
figure(AT_plot);
lgd = {'TSR $= 10$', ...
       'TSR $= 6.7$', ...
       'TSR $= 4.2$'};
legend(lgd, L, 'NorthEast', FS, def_FS-7) 
xmin = -1;
xmax = 1.32;
dx_ticks = 0.5;
xlim([xmin,xmax])
xticks(xmin:dx_ticks:xmax)
ymin = 0.4;
ymax = 1.05;
dy_ticks = 0.2;
ylim([ymin, ymax])
yticks(ymin:dy_ticks:ymax)
axis = gca;
axis.XAxis.MinorTick = 'on';
axis.YAxis.MinorTick = 'on';
axis.FontSize = def_FS - 2;
ylabel('$U/U_{ref}$', FS, def_FS)
xlabel('$x/D$', FS, def_FS)
% order = get(axis, 'Children');
% set(axis, 'Children', flipud(order))
%title_text = 'Axial induction - $t: 5-15s$ - $r/R = -0.82$ - $1.5$M cells - $\varepsilon_R = 0.2$ - $\varepsilon_T = 0.1$';
%title(title_text, 'Interpreter', 'latex')

%% Create textboxs
annotation(AT_plot,'textbox',...
    [0.2 0.2 0.075 0.05],...
    'String','Tower',...
    'Interpreter','latex',...
    'FontSize',13,...
    'FontName','Helvetica Neue',...
    'LineWidth',1.5,...
    'BackgroundColor','w',...
    'EdgeColor',tower_color,...
    'FitBoxToText','off');

annotation(AT_plot,'textbox',...
    [0.43 0.2 0.074 0.05],...
    'String','Rotor',...
    'Interpreter','latex',...
    'FontSize',13,...
    'FontName','Helvetica Neue',...
    'LineWidth',1.5,...
    'BackgroundColor','w',...
    'EdgeColor',rotor_color,...
    'FitBoxToText','off');

%% Saving the AT plot
width = 8.5;
height = 5.5;
SavePlot(AT_plot, 'AxialTraverses', 'pdf', width, height)
