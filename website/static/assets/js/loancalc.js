// Referencing the input fields (Amount, Interest rate and tenure)
const loanAmountInput = document.querySelector(".loan-amount");
const interestRateInput = document.querySelector(".interest-rate");
const loanTenureInput = document.querySelector(".loan-tenure");

// Referencing the values (EMI Value, total interest value, loan amount value)
const loanEMIValue = document.querySelector(".loan-emi .value");
const totalInterestValue = document.querySelector(".total-interest .value");
const totalAmountValue = document.querySelector(".total-amount .value");

// Referencing the calculate button
const calculateBtn = document.querySelector(".calculate-btn");

// Converting the values gotten in the input fields into a number
let loanAmount = parseFloat(loanAmountInput.value);
let interestRate = parseFloat(interestRateInput.value);
let loanTenure = parseFloat(loanTenureInput.value);

// variable to calculate r
let interest = interestRate / 12 / 100;

let myChart;

// Input validation
const checkValues = () => {
    let loanAmountValue = loanAmountInput.value;
    let interestRateValue = interestRateInput.value;
    let loanTenureValue = loanTenureInput.value;
  
    let regexNumber = /^[0-9]+$/; // creating a regular expression for integers
    if (!loanAmountValue.match(regexNumber)) {
      loanAmountInput.value = "10000";
    }
  
    if (!loanTenureValue.match(regexNumber)) {
      loanTenureInput.value = "12";
    }
  
    let regexDecimalNumber = /^(\d*\.)?\d+$/; // creating a regular expression for decimal values
    if (!interestRateValue.match(regexDecimalNumber)) {
      interestRateInput.value = "7.5";
    }
  };

// Function to display chart
const displayChart = (totalInterestPayableValue) => {
const ctx = document.getElementById("myChart").getContext("2d");
myChart = new Chart(ctx, {
    type: "pie",
    data: {
    labels: ["Total Interest", "Principal Loan Amount"],
    datasets: [
        {
        data: [totalInterestPayableValue, loanAmount],
        backgroundColor: ["#7CFC00", "#3589f1"],
        borderWidth: 0,
        },
    ],
    },
});
};

// Function for updating the chart
const updateChart = (totalInterestPayableValue) => {
    myChart.data.datasets[0].data[0] = totalInterestPayableValue;
    myChart.data.datasets[0].data[1] = loanAmount;
    myChart.update();
};

// Function to update all the values
const refreshInputValues = () => {
    loanAmount = parseFloat(loanAmountInput.value);
    interestRate = parseFloat(interestRateInput.value);
    loanTenure = parseFloat(loanTenureInput.value);
    interest = interestRate / 12 / 100;
};

// Function to calculate the EMI
// Loan amount = P, Interest = r, Loan tenure = n
const calculateEMI = () => {
checkValues();
refreshInputValues();
let emi =
    loanAmount *
    interest *
    (Math.pow(1 + interest, loanTenure) /
    (Math.pow(1 + interest, loanTenure) - 1));

return emi;
};

// Function that updates all the values 
const updateData = (emi) => {
    loanEMIValue.innerHTML = Math.round(emi);

    let totalAmount = Math.round(loanTenure * emi);
    totalAmountValue.innerHTML = totalAmount;

    let totalInterestPayable = Math.round(totalAmount - loanAmount);
    totalInterestValue.innerHTML = totalInterestPayable;

if (myChart) {
    updateChart(totalInterestPayable);
} else {
    displayChart(totalInterestPayable);
}
};

const init = () => {
    let emi = calculateEMI();
    updateData(emi);
  };
  
  init();

// Event listener for calculate button
calculateBtn.addEventListener("click", init);