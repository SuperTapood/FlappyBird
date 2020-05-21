import cx_Freeze


# create an exe from file "FAN.py"
executables = [cx_Freeze.Executable("FlappyBird.py")]


# setup cx_Freeze
cx_Freeze.setup(
	name="FlappyBird",
	options={"build_exe": {"packages": ["pygame"], 
							"include_files": ["imgs"]}},
	executables=executables
	)