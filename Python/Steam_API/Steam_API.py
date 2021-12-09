from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Games(Resource):
    def get(self):
        data = pd.read_csv('steam_data/steam.csv')
        data = data.to_dict()
        return {'data': data}, 200
    
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('appid', required = True)
        parser.add_argument('name', required = True)
        parser.add_argument('release_date', required = False)
        parser.add_argument('english', required = False)
        parser.add_argument('developer', required = True)
        parser.add_argument('publisher', required = False)
        parser.add_argument('platforms', required = False)
        parser.add_argument('required_age', required = False)
        parser.add_argument('categories', required = False)
        parser.add_argument('genres', required = False)
        parser.add_argument('steamspy_tags', required = False)
        parser.add_argument('achievements', required = False)
        parser.add_argument('positive_ratings', required = False)
        parser.add_argument('negative_ratings', required = False)
        parser.add_argument('average_playtime', required = False)
        parser.add_argument('median_playtime', required = False)
        parser.add_argument('owners', required = False)
        parser.add_argument('price', required = False)
        
        args = parser.parse_args()
        
        data = pd.read_csv('steam_data/steam.csv')
        
        if args['appid'] in list(data['appid']):
            return {'App ID': f"'{args['appid']}' already exists."}, 409
        else:
            new_data = pd.DataFrame({
                'appid' : [args['appid']],
                'name' : [args['name']],
                'release_date' : [args['release_date']],
                'english' : [args['english']],
                'developer' : [args['developer']],
                'publisher' : [args['publisher']],
                'required_age' : [args['required_age']],
                'categories' : [args['categories']],
                'genres' : [args['genres']],
                'steamspy_tags' : [args['steamspy_tags']],
                'achievements' : [args['achievements']],
                'positive_ratings' : [args['positive_ratings']],
                'negative_ratings' : [args['negative_ratings']],
                'average_playtime' : [args['average_playtime']],
                'median_playtime' : [args['median_playtime']],
                'owners' : [args['owners']],
                'price' : [args['price']]
            })
            
            data = data.append(new_data, ignore_index=True)
            data.to_csv('steam_data/steam.csv', index=False)
            return {'data' : data.to_dict()}, 200
        
    def put(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('appid', required = True)
        parser.add_argument('name', required = False)
        parser.add_argument('release_date', required = False)
        parser.add_argument('english', required = False)
        parser.add_argument('developer', required = False)
        parser.add_argument('publisher', required = False)
        parser.add_argument('platforms', required = False)
        parser.add_argument('required_age', required = False)
        parser.add_argument('categories', required = False)
        parser.add_argument('genres', required = False)
        parser.add_argument('steamspy_tags', required = False)
        parser.add_argument('achievements', required = False)
        parser.add_argument('positive_ratings', required = False)
        parser.add_argument('negative_ratings', required = False)
        parser.add_argument('average_playtime', required = False)
        parser.add_argument('median_playtime', required = False)
        parser.add_argument('owners', required = False)
        parser.add_argument('price', required = False)
        
        args = parser.parse_args()
        
        data = pd.read_csv('steam_data/steam.csv')
        
        if args['appid'] in list(data['appid']):
            
            row_data = data[data['appid'] == args['appid']]
            
            row_data['name'] = row_data['name'].append(args['name'])
            row_data['release_date'] = row_data['release_date'].append(args['release_date'])
            row_data['english'] = row_data['english'].append(args['english'])
            row_data['developer'] = row_data['developer'].append(args['developer'])
            row_data['publisher'] = row_data['publisher'].append(args['publisher'])
            row_data['required_age'] = row_data['required_age'].append(args['required_age'])
            row_data['categories'] = row_data['categories'].append(args['categories'])
            row_data['genres'] = row_data['genres'].append(args['genres'])
            row_data['steamspy_tags'] = row_data['steamspy_tags'].append(args['steamspy_tags'])
            row_data['achievements'] = row_data['achievements'].append(args['achievements'])
            row_data['positive_ratings'] = row_data['positive_ratings'].append(args['positive_ratings'])
            row_data['negative_ratings'] = row_data['negative_ratings'].append(args['negative_ratings'])
            row_data['average_playtime'] = row_data['average_playtime'].append(args['average_playtime'])
            row_data['median_playtime'] = row_data['median_playtime'].append(args['median_playtime'])
            row_data['owners'] = row_data['owners'].append(args['owners'])
            row_data['price'] = row_data['price'].append(args['price'])
            
            data.to_csv('steam_data/steam.csv', index=False)
            return {'data' : data.to_dict()}, 200
        
        else:
            return {'message' : f"'{args['appid']}' app id not found." }, 404
            
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('appid', required = True)
        args = parser.parse_args()

        data = pd.read_csv('steam_data/steam.csv')
        print(list(data['appid']), 'args:', args['appid'])
        
        if args['appid'] in list(data['appid']):
            data = data[data['appid'] != args['appid']]
            data.to_csv('steam_data/steam.csv', index=False)
            return {'data' : data.to_dict()}, 200
        else:
            return {'message' : f"'{args['appid']}' app id not found"}, 404

api.add_resource(Games, '/games')

if __name__ == '__main__':
    app.run()