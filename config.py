__author__ = 'nessumo'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alpha:alpha@localhost:5555/yggdev'
SQLALCHEMY_BINDS = {
    'jira': 'postgresql+psycopg2://jirauser:jirauser@localhost:5555/jira'
}