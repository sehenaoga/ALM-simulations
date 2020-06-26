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
%Runs = {'Run3', 'Run5', 'Run6', 'Run7', 'Run8', 'Run9', 'Run10'}; %V10, V15, V24 m/s results
%eps = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4];

Runs = {'Run3', 'Run5', 'Run6'}; %V10, V15, V24 m/s results
eps = [0.1, 0.15, 0.2];

%% Tower location
y_tower = 0:0.1:1.5;
x_tower = 0*y_tower;

%% Reading experimental data
%Axial traverses
AT_exp_path = 'ExperimentalData/AxialTraverses/AxialTraverses.csv';
Vars = {'V10_X','V10_Y'};
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
plot(x_tower, y_tower, LW, 1.5, C, tower_color, 'HandleVisibility','off');
hold on

%% Plotting the experimental results
%Axial traverses
figure(AT_plot)
bullets = {'ok', 'sk', '^k'};
plot(AT_exp{1}(:,1), AT_exp{1}(:,2), bullets{1}, MS, def_MS); hold on

%% Analyzing the axial traverses
%Folder = '/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/';
Folder = '/Users/Sebastian/Documents/ALM-simulations/Simulations/MEXICO/Publication/';
Subfolder = '/Postprocessing/';
%AT = {'AT1', 'AT2', 'AT3'};
AT = {'AT0'};
LS_array = {'-k'; '--k'; '-.k'; ':k'; '-b'; '--b'; '-.b'};
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
    plot(AT_num(:,1), AT_num(:,2), LS_array{i}, LW, def_LW)
    hold on
    
    %Computing the MSE
    n = size(AT_exp{1},1);
    dx = abs(AT_num(1,1) - AT_num(2,1));
    sum = 0;
    for j = 1:n
        index = round(((AT_exp{1}(j,1)-AT_num(1,1))/dx)+1);
        if index < 0
            index = 1;
        elseif index > size(AT_num,1)
            index = size(AT_num,1);
        end
        diff = (AT_exp{1}(j,2) - AT_num(index,2))^2;
        sum = sum + diff;
    end
    MSE(i) = 1/n*sum;
end
MSE = MSE';

%% Labeling the AT plot
figure(AT_plot);
lgd = {'Experimental data'};
for i = 2:size(eps,2)+1
    lgd{i} = strcat('$\varepsilon = ', num2str(eps(i-1)), '$');
end
legend(lgd, L, 'SouthWest', FS, def_FS-7) 
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
axis.FontSize = def_FS - 2;
ylabel('$U/U_{ref}$', FS, def_FS)
xlabel('$x/D$', FS, def_FS)
% order = get(axis, 'Children');
% set(axis, 'Children', flipud(order))
%title_text = 'Axial induction - $t: 5-15s$ - $r/R = 0.82$ - $1.5$M cells - $\varepsilon_R = 0.2$ - $\varepsilon_T = 0.1$';
%title(title_text, 'Interpreter', 'latex')

%% Saving the AT plot
%figure(AT_plot)
%set(gcf, 'Units', 'inches', 'Position', [5, 5, 5.6, 3.6], 'PaperSize', [5.7,3.7])
%saveas(AT_plot, 'Axial traverses', 'png');
width = 8.5;
height = 5.5;
SavePlot(AT_plot, 'AxialTraverses', 'pdf', width, height)
