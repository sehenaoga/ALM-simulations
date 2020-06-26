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
Runs = {'Run19', 'Run20', 'Run21'}; %V10, V15, V24 m/s results

%% Rotor location
Rotor_0 = [15, 11.25, 5];
y_rotor = 0:0.1:1.5;
x_rotor = 0*y_rotor;

Tower_0 = (12-15)/4.5; %Downwind
y_tower = 0:0.1:1.5;
x_tower = 0*y_tower+Tower_0;

%% Plotting the rotor location
AT_plot = figure();
rotor_color = '#ACACAC';
plot(x_rotor, y_rotor, '-', LW, 1, C, rotor_color, 'HandleVisibility','off');
hold on

%% Plotting the tower location
figure(AT_plot)
tower_color = '#ACACAC';
plot(x_tower, y_tower, '-', LW, 1, C, tower_color, 'HandleVisibility','off');
hold on

%% Analyzing the axial traverses
figure(AT_plot)
Folder = '/media/Data/ALM/ALM-simulations/Simulations/MEXICO/Publication/';
Subfolder = '/Postprocessing/AT/';
AT = {'AT1', 'AT2', 'AT3'};
LS_array = {'-'; '--'; '-.'};
for i = 1:size(Runs,2)
    %Reading the data
    for j = 1:size(AT,2)
        PATH = strcat(Folder, Runs{i}, Subfolder, AT{j}, '.csv');
        Vars = {'Points_0', 'U_0'};
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
end


%% Labeling the AT plot
figure(AT_plot);
lgd = legend('$U_{in} = 10 \ m/s$', ... 
             '$U_{in} = 15 \ m/s$', ...
             '$U_{in} = 24 \ m/s$');
set(lgd, 'Interpreter', 'latex')
set(lgd, 'Location', 'southwest') 
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
ylabel('$a = U/U_{ref}$')
xlabel('$x/D$')
title_text = 'Axial induction - $t: 5-15s$ - $r/R = -0.82$ - $1.5$M cells - $\varepsilon_R = 0.2$ - $\varepsilon_T = 0.1$';
title(title_text, 'Interpreter', 'latex')
%% Saving the AT plot
figure(AT_plot)
set(gcf, 'Units', 'inches', 'Position', [5, 5, 5.6, 3.6], 'PaperSize', [5.7,3.7])
saveas(AT_plot, 'Axial traverses', 'pdf');

