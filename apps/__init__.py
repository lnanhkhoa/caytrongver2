# coding=utf-8

import os
from flask import Flask, render_template

app = Flask(__name__)

import apps.view
import apps.api