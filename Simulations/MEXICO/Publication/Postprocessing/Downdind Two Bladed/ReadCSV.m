function Vars_extracted=ReadCSV(PATH,Vars_preserve,disp_vars)
%% Reading CSV
Table = readtable(PATH, 'ReadVariableNames', true);
%Table = readtable(PATH);
Vars_extracted = [];
if disp_vars
    Vars_list = Table.Properties.VariableNames
else
    n = size(Vars_preserve, 2);
    for i=1:n
        Vars_extracted(:,i) = Table.(Vars_preserve{i});
    end
    
end