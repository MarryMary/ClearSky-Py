from Core.Elena.Router.StarNavigator import StarNavigator
from Core.Elena.Executer.Provide import Provide
# Sample
# StarNavigator::Get("/", function(){ echo "hello"; };)
StarNavigator.Get("/", lambda env, start_response: Provide.echo(start_response, Provide.Viewer("Hello")))