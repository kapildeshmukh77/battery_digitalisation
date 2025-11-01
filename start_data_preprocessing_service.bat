@echo off

CALL conda activate digital-dryroom
echo "running preprocessing service"
run-data-processing-service

pause