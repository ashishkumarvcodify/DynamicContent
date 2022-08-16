# code
  ### - HTML
  ### - Bootstrap
  
## Base.html
  - this page created where common tags is defined that needs to be load every where
  
### {% block content %}__code__{% endblock %}
  it is use to load the te cntent of the current html page. code should be written between this tag so it will work
  
### {% block content %}{% endblock 
   this tag needs to be defined in base.html where another pages code needs to be run

### {% extends 'base.html' %}
  with this tag we can load the base.html file content in the current page. it should be written on top of the page.
