var report = swan.loadAnalysis("Return and Correlation");
var returnCalcs = report.get("Return Calc Options");
returnCalcs.setCostBasisTreatment("Business Unit Capital");
report.get("ViewChooser").setViewName("BU-SBU-Strat-Und-Sym");
report.get("PortfolioSelector").setBooking(["GLEA"], ["EC", "HG", "HY", "LOANS"], ["HGNI", "HYNI"], []);
report.get("ForestSelector").selectDepth(1);
report.get("ForestSelector").addPaths(["root"]);

var observablesInput = new Array();
var observablesSWAN = new Array();
var observablesReport = report.get("ObservableChooser");
observablesInput.push(["JXEME Index", "JPM xs Ret", "JPM xs Ret"]);
observablesInput.push(["JPDDHYI Index", "JPM US HY", "JPM US HY"]);

for (var i = 0; i < observablesInput.length; i++) {
      iObservable = observablesInput[i];
      observablesReport.create(iObservable);
      observablesSwan.push(iObservable[1]);
}
