import pandas as pd

from openpyxl.styles import Font

from api_client import get_receiving_report


DATE = "2026-09-22"


def get_delivery_status(difference):
    if difference < 0:
        return "Short delivery"
    elif difference == 0:
        return "Complete"
    else:
        return "Over delivery"


def auto_adjust_width(sheet):
    for column in sheet.columns:
        max_length = 0

        for cell in column:
            if cell.value is not None:
                max_length = max(
                    max_length,
                    len(str(cell.value)),
                )

        sheet.column_dimensions[
            column[0].column_letter
        ].width = max_length + 2


def main():
    report = get_receiving_report(DATE)

    df = pd.DataFrame(report["rows"])

    report_df = df[
        [
            "poNumber",
            "supplier",
            "articleNumber",
            "product",
            "quantityOrdered",
            "quantityReceived",
            "remainingQuantity",
            "difference",
            "reasonCode",
            "actionStatus",
            "epCount",
        ]
    ].copy()

    report_df["status"] = report_df["difference"].apply(
        get_delivery_status
    )

    summary = report["summary"]

    summary_df = pd.DataFrame(
        {
            "Metric": [
                "Total Purchase Orders",
                "Total Items",
                "Total Delivered",
                "Total EP Kasser",
                "Total Discrepancies",
            ],
            "Value": [
                summary["totalPurchaseOrders"],
                summary["totalItems"],
                summary["totalDelivered"],
                summary["totalEpKasser"],
                summary["totalDiscrepancies"],
            ],
        }
    )

    output_file = "data/receiving_report.xlsx"

    with pd.ExcelWriter(
        output_file,
        engine="openpyxl",
    ) as writer:

        summary_df.to_excel(
            writer,
            sheet_name="Summary",
            index=False,
        )

        report_df.to_excel(
            writer,
            sheet_name="Receiving Report",
            index=False,
        )

        summary_sheet = writer.sheets["Summary"]
        report_sheet = writer.sheets["Receiving Report"]

        for cell in summary_sheet[1]:
            cell.font = Font(bold=True)

        for cell in report_sheet[1]:
            cell.font = Font(bold=True)

        summary_sheet.freeze_panes = "A2"
        report_sheet.freeze_panes = "A2"

        report_sheet.auto_filter.ref = report_sheet.dimensions

        auto_adjust_width(summary_sheet)
        auto_adjust_width(report_sheet)
    print(f"Report exported successfully: {output_file}")


if __name__ == "__main__":
    main()