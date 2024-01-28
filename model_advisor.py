# run_modeladvisor.py

import argparse

def run_model_advisor(model_name, prg_ver, mbd_ver):
    if prg_ver == "DAT3":
        print("Running Model Advisor for DAT3 program version.")
        # Add Model Advisor logic specific to DAT3
    elif prg_ver == "DAT4":
        print("Running Model Advisor for DAT4 program version.")
        # Add Model Advisor logic specific to DAT4
    else:
        print(f"Unsupported program version: {prg_ver}")

    # Common Model Advisor logic for all models
    print(f"Running Model Advisor for {model_name}, Program Version: {prg_ver}, MBD Version: {mbd_ver}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Model Advisor script")
    parser.add_argument("--f_name", help="Model name", required=True)
    parser.add_argument("--prg_ver", help="Program version", required=True)
    parser.add_argument("--mbd_ver", help="MBD version", required=True)

    args = parser.parse_args()

    run_model_advisor(args.f_name, args.prg_ver, args.mbd_ver)
