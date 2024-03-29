class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        #  i am given a list of strings which represents the recipes
        #  i am also give a 2d array of ingredients
        #  we can make the recipe at i if we have the ingredients available at the the same index i.
        #  the catch is some ingredients need to be made first using other recipes and ingredients
        #  this tells that there is a dependency amongst the ingredients. ie i cant make the burger recipe until i have already made the patty from another recipe and ingredient list.
        #  we can possible apply topological sorting to this problem, as well as represent the recipes and ingredients as a graph data structure.
        #  Additionally i have a list of supplies that has all the initial items we need. we wont run out of these supplies
        #  test case:
        #  recipe =  ["bread","sandwich"]
        #  ingredients = [["yeast","flour"],["bread","meat"]]
        #  supplies =  ["yeast","flour","meat"]
        #  now how can i represent this using a graph
        # we can view in this manner, an recipe is dependent on the ingredients, and the ingredients are dependent on the supplies. recipe ==> ingredients ==> supplies. We this relationship we can represent it using some type of adjecency list. where this firts key will be the recipe and foreach recipe we will keep a list of all the ingredients that are needed.
        #  From here we can check if its possible to make a recipe if we can topological sort all the elements involved
        graph = {val: i for i, val in enumerate(recipes)}
        for i, val in enumerate(ingredients):
            for key, v in graph.items():
                if i == v:
                    graph[key] = val
        cycle = set()
        visit = set()
        output = []

        def topSort(food):
            if food in cycle:
                return False
            if food in visit:
                return True
            cycle.add(food)
            for f in graph[food]:
                if not topSort(f):
                    return False
            visit.add(food)
            cycle.remove(food)
            if food in graph:
                output.append[food]
            return True
        for r in recipes:
            if not topSort(r):
                return
        return output
