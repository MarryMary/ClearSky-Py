from Core.Elena.Router.StarNavigator import StarNavigator

# Sample
# StarNavigator::Get("/", function(){ echo "hello"; };)
StarNavigator.Get("/", lambda : print("hello"))