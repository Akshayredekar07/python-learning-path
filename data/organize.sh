#!/bin/bash

# Create the base directory structure (flat structure with numbering)
mkdir -p 00_course_materials/pdfs
mkdir -p 01_language_basics
mkdir -p 02_data_types
mkdir -p 03_functions
mkdir -p 04_modules
mkdir -p 05_packages
mkdir -p 06_oop_basics
mkdir -p 07_inheritance
mkdir -p 08_advanced_oop
mkdir -p 09_exception_handling
mkdir -p 10_file_handling
mkdir -p 11_multithreading
mkdir -p 12_decorators
mkdir -p 13_generators
mkdir -p 14_regex
mkdir -p 15_logging
mkdir -p 16_serialization
mkdir -p 17_database
mkdir -p 18_mini_projects
mkdir -p 19_practice/patterns
mkdir -p 19_practice/interview_questions


# Move the .ipynb files to their respective directories
# Language fundamentals
cp 01_language_fundamentals.ipynb 01_language_basics/
cp 02_input_output.ipynb 01_language_basics/
cp 03_operators.ipynb 01_language_basics/
cp 04_flow_control.ipynb 01_language_basics/

# Data Types
cp 05_string_basics.ipynb 02_data_types/
cp 06_string_questions.ipynb 02_data_types/
cp 07_list_data_type.ipynb 02_data_types/
cp 08_list_examples.ipynb 02_data_types/
cp 09_tuple_data_structure.ipynb 02_data_types/
cp 10_set_data_structure.ipynb 02_data_types/
cp 11_dictionary_data_structure.ipynb 02_data_types/
cp 12_dictionary_questions.ipynb 02_data_types/

# Functions and Modules
cp 13_functions.ipynb 03_functions/
cp 14_modules.ipynb 04_modules/
cp 15_packages.ipynb 05_packages/

# OOP related notebooks
cp 76_class_introduction.ipynb 06_oop_basics/
cp 77_self_variable.ipynb 06_oop_basics/
cp 78_constructor.ipynb 06_oop_basics/
cp 79_movie_example.ipynb 06_oop_basics/
cp 80_instance_methods.ipynb 06_oop_basics/
cp 81_static_variables.ipynb 06_oop_basics/
cp 82_static_variables_advanced.ipynb 06_oop_basics/
cp 83_instance_class_methods.ipynb 06_oop_basics/
cp 84_method_comparison.ipynb 06_oop_basics/
cp 85_accessing_class_members.ipynb 06_oop_basics/

# Inheritance
cp 93_inheritance_basics.ipynb 07_inheritance/
cp 94_inheritance_types.ipynb 07_inheritance/
cp 95_method_resolution_order.ipynb 07_inheritance/
cp 96_method_resolution_operator.ipynb 07_inheritance/
cp 97_super_function.ipynb 07_inheritance/
cp 98_super_usecases.ipynb 07_inheritance/

# Advanced OOP
cp 86_inner_nested_class.ipynb 08_advanced_oop/
cp 87_inner_class_examples.ipynb 08_advanced_oop/
cp 88_nested_methods.ipynb 08_advanced_oop/
cp 89_garbage_collector.ipynb 08_advanced_oop/
cp 90_destructor_questions.ipynb 08_advanced_oop/
cp 91_has_a_relationship.ipynb 08_advanced_oop/
cp 92_class_member_usage.ipynb 08_advanced_oop/
cp 99_polymorphism.ipynb 08_advanced_oop/
cp 100_operator_overloading.ipynb 08_advanced_oop/
cp 101_nested_operator_overloading.ipynb 08_advanced_oop/
cp 102_constructor_overloading.ipynb 08_advanced_oop/
cp 103_method_constructor_overriding.ipynb 08_advanced_oop/
cp 104_abstract_classes.ipynb 08_advanced_oop/
cp 105_interface_abstract_concrete.ipynb 08_advanced_oop/
cp 106_public_private_members.ipynb 08_advanced_oop/
cp 107_protected_members.ipynb 08_advanced_oop/
cp 108_data_hiding.ipynb 08_advanced_oop/
cp 109_str_rep_methods.ipynb 08_advanced_oop/

# Mini Projects
cp 110_mini_project.ipynb 18_mini_projects/
cp 111_mini_project_part1.ipynb 18_mini_projects/

# Function Decorator
cp 113_function_aliasing.ipynb 12_decorators/
cp 114_decorator_examples.ipynb 12_decorators/
cp 115_function_without_decorator.ipynb 12_decorators/

# Generators
cp 116_generators.ipynb 13_generators/
cp 117_generator_limitations.ipynb 13_generators/

# Exception Handling
cp 118_exception_handling_intro.ipynb 09_exception_handling/
cp 119_exception_hierarchy.ipynb 09_exception_handling/
cp 120_else_combinations.ipynb 09_exception_handling/
cp 121_finally_cases.ipynb 09_exception_handling/
cp 122_nested_try_except.ipynb 09_exception_handling/
cp 123_else_with_exception.ipynb 09_exception_handling/
cp 124_custom_exceptions.ipynb 09_exception_handling/

# File Handling
cp 125_file_handling_intro.ipynb 10_file_handling/
cp 126_file_read_write.ipynb 10_file_handling/
cp 127_with_statement.ipynb 10_file_handling/
cp 128_binary_data_handling.ipynb 10_file_handling/
cp 129_directory_operations.ipynb 10_file_handling/
cp 130_directory_management.ipynb 10_file_handling/

# Multithreading
cp 131_multithreading_intro.ipynb 11_multithreading/
cp 132_thread_creation.ipynb 11_multithreading/
cp 133_thread_definition_methods.ipynb 11_multithreading/
cp 134_thread_methods.ipynb 11_multithreading/
cp 135_daemon_threads.ipynb 11_multithreading/
cp 136_thread_synchronization.ipynb 11_multithreading/
cp 137_locks_semaphores.ipynb 11_multithreading/
cp 138_thread_communication_part1.ipynb 11_multithreading/
cp 139_thread_communication_part2.ipynb 11_multithreading/

# Put advanced topics in respective folders
cp 140_programming_best_practices.ipynb 01_language_basics/
cp 141_aliasing_cloning_deepcopy.ipynb 02_data_types/
cp 142_assertions.ipynb 09_exception_handling/

# Regular Expressions
cp 143_regex_basics.ipynb 14_regex/
cp 144_regex_character_classes.ipynb 14_regex/
cp 145_regex_module_functions.ipynb 14_regex/
cp 146_regex_applications.ipynb 14_regex/
cp 147_web_scraping.ipynb 14_regex/

# Database
cp 148_python_database.ipynb 17_database/
cp 151_mysql_database.ipynb 17_database/

# Serialization
cp 152_object_serialization.ipynb 16_serialization/
cp 153_serialization_part2.ipynb 16_serialization/
cp 154_coindesk_application.ipynb 16_serialization/
cp 155_yaml_serialization.ipynb 16_serialization/

# Logging
cp 156_logging_module.ipynb 15_logging/
cp 157_format_messages.ipynb 15_logging/
cp 158_custom_logging.ipynb 15_logging/

# Advanced Topics
cp 50_advanced_topics.ipynb 01_language_basics/

# Keep the Images folder as is (don't move it)
# cp -r Images Images/

# Move python class materials to course materials
cp -r Python_class/0.PDF/* 00_course_materials/pdfs/
cp pythonbook.pdf 00_course_materials/pdfs/
cp "Durga Sir Numpy.pdf" 00_course_materials/pdfs/

# Move code examples to their respective folders
cp -r Python_class/Decorator/* 12_decorators/examples/
cp -r Python_class/Generator/* 13_generators/examples/
cp -r Python_class/ExceptionHandling/* 09_exception_handling/examples/
cp -r Python_class/Function/* 03_functions/examples/
cp -r Python_class/Module_py/* 04_modules/examples/
cp -r Python_class/Package/* 05_packages/examples/
cp -r Python_class/Logging/* 15_logging/examples/
cp -r Python_class/MultiThreading/* 11_multithreading/examples/
cp -r Python_class/OOPS/* 06_oop_basics/examples/
cp -r Python_class/PyDataStructure/Dictionary/* 02_data_types/dictionary_examples/
cp -r Python_class/PyDataStructure/list_ds/* 02_data_types/list_examples/
cp -r Python_class/PyDataStructure/set/* 02_data_types/set_examples/
cp -r Python_class/PyDataStructure/tuple/* 02_data_types/tuple_examples/
cp -r Python_class/ReGex/* 14_regex/examples/
cp -r Python_class/flowControl/* 01_language_basics/flow_control_examples/
cp -r Python_class/inOut/* 01_language_basics/io_examples/
cp -r Python_class/objSerialization/* 16_serialization/examples/
cp -r Python_class/oper/* 01_language_basics/operator_examples/
cp -r Python_class/pattern/* 19_practice/patterns/
cp -r Python_class/string/* 02_data_types/string_examples/
cp -r Python_class/string_interview/* 19_practice/interview_questions/string/

# Move mini projects
cp -r "Mini Project"/* 18_mini_projects/
cp -r Patterns/* 19_practice/patterns/


# Move all the media files to their respective folders
find . -name "*.txt" -not -path "./*/examples/*" -exec cp {} data/ \;
find . -name "*.csv" -not -path "./*/examples/*" -exec cp {} data/ \;
find . -name "*.json" -not -path "./*/examples/*" -exec cp {} data/ \;
find . -name "*.jpg" -not -path "./*/examples/*" -exec cp {} data/ \;
find . -name "*.zip" -not -path "./*/examples/*" -exec cp {} data/ \;
find . -name "*.log" -not -path "./*/examples/*" -exec cp {} data// \;

echo "Directory reorganization complete!"