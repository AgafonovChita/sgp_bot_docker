from bot.models.member import MemberPydantic
from bot.services.workers.celery_worker import celery
from bot.google_sheets_api.gsheets_api import get_worksheet, WORKSHEET, member_format_update


@celery.task()
def add_record_in_lottery_list(user_id: int, username: str, code: int):
    worksheet = get_worksheet(WORKSHEET.LOTTERY_IDX)
    worksheet.append_row([user_id, username, code])


@celery.task()
def update_member_sheet(member_pydantic: MemberPydantic):
    event_data = member_format_update(member_pydantic)
    worksheet = get_worksheet(worksheet=WORKSHEET.BASIC_IDX)

    cell = worksheet.find(str(event_data[0]))

    if cell:
        for x in range(1, 13):
            worksheet.update_cell(row=cell.row, col=x, value=event_data[x - 1])
    else:
        worksheet.append_row(event_data)
