from Core.Elena.Router.StarNavigator import StarNavigator
from Core.Elena.Executer.Executer import Executer
# Sample
# StarNavigator::Get("/", function(){ echo "hello"; };)
StarNavigator.Get("/", lambda env, start_response: Executer.Viewer("Hello"))