import logging


SEPARATOR = '****'
CONTENT_STARTERS = ['\u3000', '\u300c']

logging.getLogger(__name__).addHandler(logging.NullHandler())


def pluck_title(data):
    """
    Pluck title from data.

    Title is the first non blank line from the text before line that started
    with Unicode 3000 (Ideographic Space).

    :param data: Results from merged function.
    :return: Returns title text in tuple(raw, translation).

    :type data: iterable
    :rtype: tuple

    """

    titles = tuple()
    for datum in data:
        # Skip if raw is empty.
        if not datum[0]:
            continue

        # Stop if we encountered content starter.
        if datum[0] and datum[0][0] in CONTENT_STARTERS:
            break

        # Get the datum that seems to be title.
        titles = datum

    return titles


def pluck_content(data):
    """
    Pluck content from data.

    Content is lines which raw text is started with Unicode 3000
    (Ideographic Space).

    :param data: Results from merged function.
    :return: Returns list of pre notes with each note is
        tuple(raw, translation).

    :type data: iterable
    :rtype: iterable

    """

    contents = []
    started = False
    for datum in data:
        # Start searching for content starter.
        if not started:
            if datum[0] and datum[0][0] in CONTENT_STARTERS:
                started = True
            else:
                continue

        # Start collecting content after ideographic space is found.

        # Stop if separator is found.
        if datum[0].startswith(SEPARATOR):
            break

        # Collect content
        contents.append(datum)

    return contents


def pluck_pre_note(data):
    """
    Pluck pre notes from data.

    Pre notes is lines before separator from the top which block didn't have
    raw text started with Unicode 3000 (Ideographic Space).

    :param data: Results from merged function.
    :return: Returns list of pre notes with each note is
        tuple(raw, translation).

    :type data: iterable
    :rtype: iterable

    """

    logger = logging.getLogger(__name__)

    notes = []
    for datum in data:
        # If we found separator, send previously collected data.
        # Though maybe we didn't collect any data at all.
        if datum[0].startswith(SEPARATOR):
            logger.debug(
                'Separator found before content. Returning pre-note.'
            )
            return notes

        # Because pre notes is lines that must appears before separator,
        # if we found content starter instead,
        # we can safely assumed that the data didn't have pre notes.
        if datum[0] and datum[0][0] in CONTENT_STARTERS:
            logger.debug(
                'Ideographic space found before separator. '
                'Returning empty list.'
            )
            return []

        logger.debug('Append note.')
        notes.append(datum)

    # This block should never be reached.
    # There is no separator nor ideographic space,
    # it's highly likely that the data is invalid.
    logger.warning('The data seems invalid. Please check again.')
    return []


def pluck_post_note(data):
    """
    Pluck post notes from data.

    Post notes is lines before separator from the bottom which block didn't
    have raw text started with Unicode 3000 (Ideographic Space).

    :param data: Results from merged function.
    :return: Returns list of pre notes with each note is
        tuple(raw, translation).

    :type data: iterable
    :rtype: iterable

    """

    notes = []
    tab_found = False
    separator_found = False
    for datum in data:
        # Because post notes must be after content first then separator second.

        # Search for content starter first.
        if not tab_found:
            if datum[0] and datum[0][0] in CONTENT_STARTERS:
                tab_found = True
            continue

        # Search for separator after content is found.
        if not separator_found:
            if datum[0].startswith(SEPARATOR):
                separator_found = True
            continue

        # Ideographic space then separator is found,
        # collect the rest of the lines as post note.
        # Though maybe there is no post notes at all.
        notes.append(datum)

    return notes
