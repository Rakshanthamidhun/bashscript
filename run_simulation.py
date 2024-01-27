import argparse

def run_simulation(model_name, mbd_version):
    print(f"Running simulation for model: {model_name}, MBD version: {mbd_version}")
    sim_sys_behavior()

def sim_sys_behavior():
    print("Simulating system behavior...")
    
    time_steps = range(0, 10)
    for time_step in time_steps:
        input_value = get_input_value(time_step)
        output_value = simulate_system_step(input_value)
        print(f"Time step {time_step}: Input = {input_value}, Output = {output_value}")

def get_input_value(time_step):
    return time_step * 2

def simulate_system_step(input_value):    
    system_gain = 0.5
    return system_gain * input_value

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run simulation for a model.")
    parser.add_argument("--f_name", required=True, help="Model name")
    parser.add_argument("--mbd_ver", required=True, help="MBD version")

    args = parser.parse_args()
    
    run_simulation(args.f_name, args.mbd_ver)

