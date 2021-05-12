import argparse
import json
from datetime import date, timedelta, datetime
from icalevents import icalevents, icalparser


def ical_to_json(url, start, days):
    end = start + timedelta(days=days)
    events = icalevents.events(
        url=url,
        start=start,
        end=end
    )
    events.sort(key=lambda event: icalparser.normalize(event.start))
    # for event in events:
    #     print("%s: %s" % (event.start, event.summary))
    return json.dumps(events,
                      indent=2,
                      ensure_ascii=False,
                      default=json_converter)


def json_converter(o):
    if isinstance(o, datetime):
        return o.__str__()
    elif isinstance(o, icalparser.Event):
        return event_to_dict(o)


def event_to_dict(event):
    return {
        'summary': event.summary,
        'description': event.description,
        'start': event.start,
        'end': event.end,
        'all_day': event.all_day,
        'recurring': event.recurring,
        'location': event.location,
        'private': event.private,
        'created': event.created,
        'last_modified': event.last_modified,
        'sequence': event.sequence,
        'attendee': event.attendee,
        'organizer': event.organizer
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=date.fromisoformat,
                        default=date.today())
    parser.add_argument("--days", type=int, default=365)
    parser.add_argument("url")
    args = parser.parse_args()

    print(ical_to_json(args.url, args.start, args.days))
