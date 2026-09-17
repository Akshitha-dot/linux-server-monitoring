









#!/bin/bash

echo "===== LINUX SERVER MONITORING ====="

#!/bin/bash

echo "===== LINUX SERVER MONITORING ====="

echo "Date:"
date

echo ""
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)"

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "Running Processes:"
ps aux --sort=-%cpu | head -6

echo "==================================="#!/bin/bash

echo "===== LINUX SERVER MONITORING ====="

echo "Date:"
date

echo ""
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)"

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "Running Processes:"
ps aux --sort=-%cpu | head -6

echo "==================================="#!/bin/bash

echo "===== LINUX SERVER MONITORING ====="

echo "Date:"
date

echo ""
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)"

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "Running Processes:"
ps aux --sort=-%cpu | head -6

echo "==================================="#!/bin/bash

echo "===== LINUX SERVER MONITORING ====="

echo "Date:"
date

echo ""
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)"

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "Running Processes:"
ps aux --sort=-%cpu | head -6

echo "==================================="#!/bin/bash

echo "===== LINUX SERVER MONITORING ====="

echo "Date:"
date

echo ""
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)"

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "Running Processes:"
ps aux --sort=-%cpu | head -6

echo "==================================="echo "Date:"
date

echo ""
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)"

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "Running Processes:"
ps aux --sort=-%cpu | head -6

echo "==================================="
chomod +r monitor.sh

