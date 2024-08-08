# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:27:08 2024

@author: Moustafa Mohammed
"""
reserved_keywords = [
    'and', 'or', 'nor', 'xor', 'xnor', 'nand', 'not', 'module', 'endmodule', 
    'parameter', 'localparam', 'always', 'initial', 'begin', 'case', 'default', 
    'endcase', 'end', 'if', 'else', 'posedge', 'negedge', 'reg', 'wire', 
    'buf', 'casex', 'for', 'forever', 'generate', 'genvar', 'input', 'output', 
    'inout', 'integer', 'wait', 'assign', 'bufif0', 'bufif1', 'cancel', 
    'cmos', 'dff', 'disable', 'edge', 'expect', 'expect_if', 'ifnone', 
    'input', 'inout', 'join', 'macromodule', 'nmos', 'out', 'pmos', 
    'pull0', 'pull1', 'scalared', 'small', 'specify', 'specparam', 
    'supply0', 'supply1', 'table', 'tranif0', 'tranif1', 'tri', 
    'tri0', 'tri1', 'triand', 'trior', 'tri0', 'tristate', 'unsigned'
]


print("Welcome")
while 1:
    module_name = input("Please, Enter your Design Module Name: ")
    if module_name in reserved_keywords:
        print("The name entered is a reserved keyword. Please enter a different name.")
    elif (not (module_name[0].isalpha()) or module_name[0].isdigit()):
        print("The name entered is invalid. Please enter a different name.")
    else:
        break
reserved_keywords.append(module_name)

Design_Module = open(f"E:/ITI Summer Training/Python/Project/new project/{module_name}.v","w")
TestBench_Module = open(f"E://ITI Summer Training/Python/Project/new project/{module_name}_TB.v","w")

           ###############Parameters###############
parameters_name=[]
parameters_size=[]
while 1:
    parameter_permission=int(input("Do you need any parameters (1 for yes /0 for no)? "))
    if(parameter_permission !=0 and parameter_permission !=1 ):
        print("invalid Value.Please Either 0 or 1.")
    else:
        break
if(parameter_permission == 1):
    while 1 :
        number_of_parameters=int(input("Enter number of parameters: "))
        if(number_of_parameters<=0):
            print("Invalid Value. Please Enter number greater than 0 ")            
        else:
            break
    for i in range(number_of_parameters):
        while 1:                   
            parameter_name = input(f"Parameter no {i+1} Name: ")
            if parameter_name in reserved_keywords:
                print("The name entered is a reserved keyword. Please enter a different name.")
            elif (not (parameter_name[0].isalpha()) or parameter_name[0].isdigit()):
                print("The name entered is invalid. Please enter a different name.")
            else:
                parameter_size = int(input(f"Parameter no {i+1} Size: "))
                parameters_name.append(parameter_name)
                parameters_size.append(parameter_size)
                break
    reserved_keywords.append(parameter_name)

            
            ###############Module Start & Parameters###############
index=0
Design_Module.write(f"module {module_name} \n")  
if(parameter_permission == 1):
    Design_Module.write("#(parameter ")
    for param_n in range(number_of_parameters):
        if(index != number_of_parameters-1):
            Design_Module.write(f"{parameters_name[param_n]}={parameters_size[param_n]}, ")
            index=index+1
        else:
            Design_Module.write(f"{parameters_name[param_n]}={parameters_size[param_n]})\n")
            
            ###############Inputs###############            
inputs_name=[]
inputs_size=[]
inputs_parameterized=[]
user_parameters=[]
inputs_number=int(input("Enter number of inputs : "))
for i in range(inputs_number):
    if (inputs_number == 0):
        break
    else:
        while 1:
            input_name = input(f"input no {i+1} Name: ")
            if input_name in reserved_keywords:
                print("The name entered is a reserved keyword. Please enter a different name.")
            elif (not (input_name[0].isalpha()) or input_name[0].isdigit()):
                print("The name entered is invalid. Please enter a different name.")
            else:
                break
        if(parameter_permission == 1):
            while 1:
                input_parameterized=int(input("Do you want to parametrize this input (1 for yes/0 for no) "))
                if(input_parameterized != 0 and input_parameterized !=1):
                    print("invalid Value.Please Either 0 or 1.")
                else:
                    break
                 
            if(input_parameterized == 1):
                user_parameter=input("which Parameter ? ")
                for param in parameters_name:
                    if (user_parameter == param):
                        input_size=0
            else:
                input_size = int(input(f"input no {i+1} Size: "))
                user_parameter=0
        else:    
            user_parameter=0
            input_parameterized=0
            input_size = int(input(f"input no {i+1} Size: "))
    inputs_name.append(input_name)
    inputs_size.append(input_size)
    inputs_parameterized.append(input_parameterized)
    user_parameters.append(user_parameter)
    reserved_keywords.append(input_name)
            
if(inputs_number!=0):
    Design_Module.write("(")
for input_count in range(inputs_number):
  
       Design_Module.write("\ninput ")
       if(inputs_parameterized[input_count] == 1):
           Design_Module.write(f"[{user_parameters[input_count]}-1:0] {inputs_name[input_count]}, ")
       elif(inputs_size[input_count] == 1):
            Design_Module.write(f"{inputs_name[input_count]}, ")
       else:
            Design_Module.write(f"[{inputs_size[input_count]-1}:0] {inputs_name[input_count]}, ")
    
           
                        
            ###############Outputs############### 
            
outputs_name=[]
outputs_size=[]
outputs_parameterized=[]
outputs_type=[]
user_output_parameters=[]
outputs_number=int(input("Enter number of outputs : "))
count_outputs_param=-1
for j in range(outputs_number):
    if (outputs_number == 0):
        break
    else:
        while 1:
            output_name = input(f"output no {j+1} Name: ")
            if output_name in reserved_keywords:
                print("The name entered is a reserved keyword. Please enter a different name.")
            elif (not (output_name[0].isalpha()) or output_name[0].isdigit()):
                print("The name entered is invalid. Please enter a different name.")
            else:
                break
        while 1:
            output_type = int(input("enter output type (1 for Reg / 0 for Wire) : "))
            if(output_type !=0 and output_type!=1):
                print("invalid Value.Please Either 0 or 1.")
            else:
                break
        if(parameter_permission == 1):
            while 1:
                output_parameterized=int(input("Do you want to parametrize this output (1 for yes/0 for no)  "))
                if(output_parameterized !=0 and output_parameterized != 1):
                    print("invalid Value.Please Either 0 or 1.")
                else:
                    break
            if(output_parameterized == 1):
                    user_output_parameter=input("which Parameter ? ")
                    for param in parameters_name:
                        if (user_output_parameter == param):
                            output_size=0
            else:
               output_size = int(input(f"output no {j+1} Size: "))   
               user_output_parameter=0
        else:    
            output_parameterized=0
            user_output_parameter=0
            output_size = int(input(f"output no {j+1} Size: "))
    outputs_name.append(output_name)
    outputs_size.append(output_size)
    outputs_type.append(output_type)
    outputs_parameterized.append(output_parameterized)            
    user_output_parameters.append(user_output_parameter)
    reserved_keywords.append(output_name)
            
for output_count in range(outputs_number):
    if(output_count != outputs_number-1):
        Design_Module.write("\noutput ")
        if(outputs_type[output_count] == 1):
            if(outputs_parameterized[output_count] == 1):
                Design_Module.write(f"reg [{user_output_parameters[output_count]}-1:0] {outputs_name[output_count]}, ")
            elif(outputs_size[output_count] == 1):
               Design_Module.write(f"reg {outputs_name[output_count]}, ")
            else:
                Design_Module.write(f"reg [{outputs_size[output_count]-1}:0] {outputs_name[output_count]}, ")
        else:
           if(outputs_parameterized[output_count] == 1):
               Design_Module.write(f"wire [{user_output_parameters[output_count]}-1:0] {outputs_name[output_count]}, ")
           elif(outputs_size[output_count] == 1):
              Design_Module.write(f"wire {outputs_name[output_count]}, ")
           else:
               Design_Module.write(f"wire [{outputs_size[output_count]-1}:0] {outputs_name[output_count]}, ")
    else:
        Design_Module.write("\noutput ")
        if(outputs_type[output_count] == 1):
            if(outputs_parameterized[output_count] == 1):
                Design_Module.write(f"reg [{user_output_parameters[output_count]}-1:0] {outputs_name[output_count]}\n); \n")
            elif(outputs_size[output_count] == 1):
               Design_Module.write(f"reg {outputs_name[output_count]}\n); ")
            else:
                Design_Module.write(f"reg [{outputs_size[output_count]-1}:0] {outputs_name[output_count]}\n); \n")
        else:
           if(outputs_parameterized[output_count] == 1):
               Design_Module.write(f"wire [{user_output_parameters[output_count]}-1:0] {outputs_name[output_count]}\n); \n")
           elif(outputs_size[output_count] == 1):
              Design_Module.write(f"wire {outputs_name[output_count]}\n); \n")
           else:
               Design_Module.write(f"wire [{outputs_size[output_count]-1}:0] {outputs_name[output_count]}\n); \n")

if(inputs_number == 0 and outputs_number == 0):
    Design_Module.write("();")                             
    
             ###############Design Module Write###############
while 1:             
    Circuit_type=int(input("Enter Circuit_type ( 0 for Sequential or 1 for Combinational) "))
    if (Circuit_type !=0  and Circuit_type != 1 ):
        print("invalid Value.Please Either 0 or 1.")
    else:
        break
if(Circuit_type == 1):
    Design_Module.write("\nalways@(*)\nbegin\n\n\n\n\nend")
else:
    while 1:
        synch_asynch=int(input("Enter Circuit_type ( 0 for Synchronous or 1 for Asynchronous) "))
        if (synch_asynch != 1 and synch_asynch != 0):
            print("invalid Value.Please Either 0 or 1.")
        else:
            break
    if(synch_asynch == 1):
        Design_Module.write("\nalways@( posedge clk , negedge reset)\nbegin\nif(!reset)\nbegin\n\nend\nelse\nbegin\n\nend")
    else:
        Design_Module.write("\nalways@( posedge clk )\nbegin\n\n\n\n\nend")        
Design_Module.write("\nendmodule")
Design_Module.close() 

                ###############TestBench Module Write###############

TestBench_Module.write(f"module {module_name}_TB\n();\n")

               ###############Parameters###############
if(parameter_permission == 1):
    for param_tb in range(number_of_parameters):
         TestBench_Module.write(f"localparam {parameters_name[param_tb]}={parameters_size[param_tb]};\n")

                ###############Inputs###############
for tb_input_count in range(inputs_number):
    if(inputs_parameterized[tb_input_count] == 1):
        TestBench_Module.write(f"reg [{user_parameters[tb_input_count]}-1:0] {inputs_name[tb_input_count]}_TB;\n")
    elif(inputs_size[tb_input_count] == 1):
        TestBench_Module.write(f"reg {inputs_name[tb_input_count]}_TB;\n")
    else:
        TestBench_Module.write(f"reg [{inputs_size[tb_input_count]-1}:0] {inputs_name[tb_input_count]}_TB;\n")
            
                ###############Outputs###############
for tb_output_count in range(outputs_number):
    if(outputs_parameterized[tb_output_count] == 1):
        TestBench_Module.write(f"wire [{user_output_parameters[tb_output_count]}-1:0]{outputs_name[tb_output_count]}_TB;\n")        
    elif(outputs_size[tb_output_count] == 1):
        TestBench_Module.write(f"wire {outputs_name[tb_output_count]}_TB;\n")
    else:
        TestBench_Module.write(f"wire [{outputs_size[tb_output_count]-1}:0]{outputs_name[tb_output_count]}_TB;\n")
    
                ###############Instantiation###############
if(parameter_permission == 1):
    TestBench_Module.write(f"{module_name} ")
    TestBench_Module.write("#(")
    for param_tb_inst in range(number_of_parameters):
        if(param_tb_inst != number_of_parameters-1):
            TestBench_Module.write(f".{parameters_name[param_tb_inst]}({parameters_name[param_tb_inst]}),")
        else:
            TestBench_Module.write(f".{parameters_name[param_tb_inst]}({parameters_name[param_tb_inst]}))")
    TestBench_Module.write(f" {module_name}_TB ")        
else:
    TestBench_Module.write(f"{module_name} {module_name}_TB ")
    
if(inputs_number != 0 and outputs_number !=0):   
    TestBench_Module.write("(")
    for tb_input_count_inst in range(inputs_number):
        TestBench_Module.write(f".{inputs_name[tb_input_count_inst]}({inputs_name[tb_input_count_inst]}_TB),")
    for tb_output_count_inst in range(outputs_number):
        if(tb_output_count_inst != outputs_number-1):
            TestBench_Module.write(f".{outputs_name[tb_output_count_inst]}({outputs_name[tb_output_count_inst]}_TB),")            
        else:
            TestBench_Module.write(f".{outputs_name[tb_output_count_inst]}({outputs_name[tb_output_count_inst]}_TB) );")
                
            ###############Clock Generation for Sequential && Test Cases###############
if(Circuit_type == 1):
    TestBench_Module.write("\n\ninitial\nbegin\n\n\n\n\nend")
else:
    TestBench_Module.write("\n\nalways\nbegin\n\n\n\n\nend")
    TestBench_Module.write("\n\ninitial\nbegin\n\n\n\n\nend")

TestBench_Module.write("\n\nendmodule")  
TestBench_Module.close()
