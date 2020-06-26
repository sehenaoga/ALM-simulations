function [] = SavePlot(fig, name, ext, width, height)
save = true;
if save 
    %% Saving the residuals plot
    figure(fig)
    %height = 8.5;
    %width = 5.5;
    set(gcf, 'Units', 'inches', 'Position', [5, 5, width, height], 'PaperSize', [width, height])
    saveas(fig, name, ext);
end