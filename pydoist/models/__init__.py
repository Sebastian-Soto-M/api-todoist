from __future__ import annotations

from typing import Any, Dict, List, Optional, Set

from pydantic import BaseModel

from requests.models import Response


class ProjectObjectModel(BaseModel):
    id: int
    name: str
    color: int
    parent_id: Optional[int]
    child_order: int
    collapsed: bool
    shared: bool
    legacy_parent_id: Optional[int]
    sync_id: Optional[int]
    is_deleted: bool
    is_archived: bool
    is_favorite: bool


class SectionModel(BaseModel):
    id: int
    name: str
    project_id: int
    legacy_project_id: Optional[int]
    section_order: int
    collapsed: bool
    user_id: int
    sync_id: Any
    is_deleted: bool
    is_archived: bool
    date_archived: Any
    date_added: str


class ItemModel(BaseModel):
    id: int
    legacy_id: Optional[int]
    user_id: int
    project_id: int
    legacy_project_id: Optional[int]
    content: str
    description: str
    priority: int
    due: Any
    parent_id: Any
    legacy_parent_id: Optional[Any]
    child_order: int
    section_id: Any
    day_order: Optional[int]
    collapsed: bool
    labels: List[int]
    added_by_uid: int
    assigned_by_uid: Optional[int]
    responsible_uid: Optional[int]
    checked: bool
    in_history: bool
    is_deleted: bool
    sync_id: Optional[int]
    date_added: str


class Features(BaseModel):
    beta: int
    dateist_inline_disabled: bool
    dateist_lang: Any
    gold_theme: bool
    has_push_reminders: bool
    karma_disabled: bool
    karma_vacation: bool
    restriction: int


class TzInfo(BaseModel):
    gmt_string: str
    hours: int
    is_dst: int
    minutes: int
    timezone: str


class UserModel(BaseModel):
    auto_reminder: int
    avatar_big: str
    avatar_medium: str
    avatar_s640: str
    avatar_small: str
    business_account_id: int
    daily_goal: int
    date_format: int
    dateist_inline_disabled: bool
    dateist_lang: Any
    days_off: List[int]
    default_reminder: str
    email: str
    features: Features
    full_name: str
    id: int
    image_id: str
    inbox_project: int
    is_biz_admin: bool
    is_premium: bool
    join_date: str
    karma: int
    karma_trend: str
    lang: str
    legacy_inbox_project: Optional[int]
    legacy_team_inbox: Optional[int]
    mobile_host: Any
    mobile_number: Any
    next_week: int
    premium_until: Any
    share_limit: int
    sort_order: int
    start_day: int
    start_page: str
    team_inbox: int
    theme: int
    time_format: int
    token: str
    tz_info: TzInfo


class Due(BaseModel):
    date: str
    timezone: str
    is_recurring: bool
    string: str
    lang: str


class ReminderModel(BaseModel):
    id: int
    notify_uid: int
    item_id: int
    service: str
    type: str
    due: Due
    mm_offset: int
    is_deleted: int


class FileAttachment(BaseModel):
    file_type: str
    file_name: str
    file_size: int
    file_url: str
    upload_state: str


class NoteModel(BaseModel):
    id: int
    legacy_id: Optional[int]
    posted_uid: int
    project_id: int
    legacy_project_id: Optional[int]
    legacy_item_id: Optional[int]
    content: str
    file_attachment: Optional[FileAttachment]
    is_deleted: bool
    posted: str
    reactions: Optional[Dict[str, List[int]]]
    uids_to_notify: List[int]
