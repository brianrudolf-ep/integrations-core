# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from typing import Any, Dict, Generator, List, Tuple

from six import iteritems

from .common import build_metric_to_submit, is_metric


def parse_summary_request_resource_metrics(data, tags):
    #  type: (Dict[str, Any], List[str]) -> Generator[Tuple, None, None]
    # TODO: iterate
    list_summary = data['request-default-list']['list-summary']

    for key, value in iteritems(list_summary):
        if is_metric(value):
            metric = build_metric_to_submit("request.{}".format(key), value, tags)
            if metric is not None:
                yield metric
