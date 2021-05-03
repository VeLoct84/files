from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

from flask import Flask, render_template, request
from flatmates_bill import flat

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        # render the main Homepage with class flask.render_template()
        return render_template("index.html")


class BillFormPage(MethodView):
    def get(self):
        # refer class BillForm()
        bill_form = BillForm()
        # render the BillFormPage with class flask.render_template()
        return render_template("bill_form_page.html", billform=bill_form)


class ResultsPage(MethodView):
    # POST request function
    def post(self):
        # BillForm with child class flask.request.form() to extract data
        billform = BillForm(request.form)

        # refer flat.py class
        the_bill = flat.Bill(float(billform.amount.data), billform.period.data)
        # assign variable for flatmate1 and flamate2
        flatmate1 = flat.Flatmate(
            billform.name1.data, float(billform.days_in_house1.data)
        )
        flatmate2 = flat.Flatmate(
            billform.name2.data, float(billform.days_in_house2.data)
        )

        return render_template(
            "results.html",
            name1=flatmate1.name,
            amount1=flatmate1.pays(the_bill, flatmate2),
            name2=flatmate2.name,
            amount2=flatmate2.pays(the_bill, flatmate1),
        )


class BillForm(Form):
    # properties interface using StringField() class
    amount = StringField("Bill Amount: ", default="100")
    period = StringField("Bill Period: ", default="April 2021")

    # ask user1 to keyin data
    name1 = StringField("Name: ", default="Mardhiah")
    days_in_house1 = StringField("Days in the house: ", default="20")

    # ask user2 to keyin data
    name2 = StringField("Name: ", default="Abdul Muiz")
    days_in_house2 = StringField("Days in the house: ", default="12")

    # add button refer to ResultPage()
    button = SubmitField("Result")


# Flask.add_url_rule() refer to class
app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill_form", view_func=BillFormPage.as_view("bill_form_page"))
app.add_url_rule("/results", view_func=ResultsPage.as_view("results_page"))


app.run(debug=True)
