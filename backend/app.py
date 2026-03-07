from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

services = [
"Basic Full Body Checkup",
"Advanced Full Body Checkup",
"Cardiac Care Panel",
"Diabetes Panel",
"Renal (Kidney) Panel",
"Liver Panel",
"Anemia Panel",
"Fever Panel",
"Infertility Panel",
"Thyroid Panel",
"Basic Pre-Surgery Panel"
]

packages = [
{
"name":"Basic Health Package",
"price":"₹999",
"tests":"Blood Sugar, CBC, Urine Routine"
},
{
"name":"Advanced Health Package",
"price":"₹1999",
"tests":"Lipid Profile, LFT, KFT, CBC"
},
{
"name":"Executive Health Package",
"price":"₹3499",
"tests":"Full Body Screening + Hormones"
}
]

@app.route("/")
def home():
    return render_template("index.html", services=services)

@app.route("/services")
def services_page():
    return render_template("services.html", services=services)

@app.route("/packages")
def packages_page():
    return render_template("packages.html", packages=packages)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
