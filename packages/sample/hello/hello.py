def main(args):
      name = args.get("name", "giu")
      greeting = "Hello " + name + "!"
      print(greeting)
      return {"body": greeting}
  
