import csv

total_months = 0
net_total = 0
previous_profit_loss = None
monthly_changes = []
months = []

with open('PyBank\\Resources\\budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvfile)

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        # The total number of months included in the dataset
        total_months += 1

        # The net total amount of "Profit/Losses" over the entire period
        net_total += profit_loss

        # The change in profit/loss since the previous month
        if previous_profit_loss is not None:
            monthly_change = profit_loss - previous_profit_loss
            monthly_changes.append(monthly_change)
            months.append(date)

        previous_profit_loss = profit_loss

if total_months > 1:
    # The average change in profit/loss
    average_change = sum(monthly_changes) / len(monthly_changes)
    average_change = round(average_change, 2)

    # The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(monthly_changes)
    greatest_increase_month = months[monthly_changes.index(greatest_increase)]

    # The greatest decrease in profits (date and amount) over the entire period
    greatest_decrease = min(monthly_changes)
    greatest_decrease_month = months[monthly_changes.index(greatest_decrease)]

    # Print the results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}") 
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

    # export a text file with the results
    with open('financial_analysis.txt', 'w') as output_file:
        output_file.write("Financial Analysis\n")
        output_file.write("------------------\n")
        output_file.write(f"Total Months: {total_months}\n")
        output_file.write(f"Total: ${net_total}\n")
        output_file.write(f"Average Change: ${average_change:.2f}\n")
        output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
        output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

    print("Results have been written to 'financial_analysis.txt'")