from flask_restx import Namespace, Resource

api = Namespace("tweets")


@api.route("/hello")
class TweetResource(Resource):
    def get(self):
        return "Hello hello from the 'tweets' namespace!"
