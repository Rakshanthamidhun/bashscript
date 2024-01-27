% model_creation.m
model = 'MySimulinkModel';
open_system(new_system(model, 'Model'));
% Add blocks, configure parameters, etc.
save_system(model, [model '.slx']);
