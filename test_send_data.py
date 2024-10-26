from send_data import send_data
from unittest.mock import patch

@patch('requests.post')
def test_send_data(mock_post):
    mock_post.return_value.status_code = 200
    data = {"patient_id": "123456", "results": "5.5"}
    send_data(data)
    mock_post.assert_called_once_with(
        "http://0.0.0.0:80/api/v1/analysis/data",
        json=data,
        headers={"Authorization": "Bearer tu_token", "Content-Type": "application/json"}
    )
