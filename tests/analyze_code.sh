#!/bin/bash

   # Check if a file is provided
   if [ -z "$1" ]; then
     echo "Usage: $0 <python_file>"
     exit 1
   fi

   PYTHON_FILE=$1

   # Check if the file exists
   if [ ! -f "$PYTHON_FILE" ]; then
     echo "File not found: $PYTHON_FILE"
     exit 1
   fi

   echo "Analyzing $PYTHON_FILE for performance and style issues..."

   # Run pylint for performance and style checks
   echo "Running pylint..."
   pylint $PYTHON_FILE

   # Run flake8 for style checks
   echo "Running flake8..."
   flake8 $PYTHON_FILE

   echo "Analysis complete."