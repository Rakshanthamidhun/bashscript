import matlab.engine

# Start MATLAB engine
eng = matlab.engine.start_matlab()

try:
    # Create a new Simulink model
    model_name = 'MySimulinkModel'
    eng.new_system(model_name, 'Model')

    # Add a block to the model
    block_name = 'MyBlock'
    eng.add_block('built-in/Note', f'{model_name}/{block_name}', nargout=0)

    # Save the model
    eng.save_system(model_name)

    # Open the model in Simulink
    eng.open_system(model_name, nargout=0)

finally:
    # Stop the MATLAB engine
    eng.quit()
