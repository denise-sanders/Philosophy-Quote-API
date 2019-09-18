from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import sqlalchemy 

db_connect = create_engine('sqlite:///test.db', echo=True)

if __name__ == '__main__':
    with open("quotes.txt") as f:
    # f=open("quotes.txt", "r")
        # f1 = f.readLines()
        # lines = [line.rstrip('\n') for line in open('filename')]
        lines = [line.rstrip('\n') for line in open('quotes.txt')]
        conn = db_connect.connect()
        for x in lines:
            parts = x.split(";")
            if len(parts) == 3:
                command = 'insert into quote (quote, source, philosopher) values ("{}", "{}", "{}");'.format(parts[0],parts[1],parts[2])
                conn.execute(command)
                # print("something")
            elif len(parts) >3:
                quotePart = parts[:-2]
                quote = ";".join(quotePart)
                # print(quote)
                command = 'insert into quote (quote, source, philosopher) values ("{}", "{}", "{}");'.format(quote,parts[-2],parts[-1])
                conn.execute(command)
            elif len(parts) <3:
                print(x)

     
