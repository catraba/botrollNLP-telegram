from utils.constants import model, tokenizer



def get_sexist_res(msg: str) -> bool:
    tokenized_text = tokenizer(
        msg,
        truncation = True,
        return_tensors = 'pt'
    )

    outputs = model(tokenized_text['input_ids'])

    predicted_label = outputs.logits.argmax(-1)

    return predicted_label.item() == 1