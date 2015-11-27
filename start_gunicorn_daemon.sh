#!/bin/bash
gunicorn kalkulator.wsgi --daemon --reload
