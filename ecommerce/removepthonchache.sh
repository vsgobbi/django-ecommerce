#!/bin/bash
find . -name "*.pyc" -exec rm -rf {} \;
echo "Remove cached files..."
