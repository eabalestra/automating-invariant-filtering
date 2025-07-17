#!/bin/bash

coverage run --branch --source='src/' -m pytest
coverage html