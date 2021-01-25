# training test
import sentencepiece as spm

#sp = spm.SentencePieceProcessor(model_file='ulm_test.model')
# spm.SentencePieceTrainer.train(input='youku_continuous_none_tagged_tmp.txt', model_prefix='ulm_test',
#                                vocab_size=4861, split_by_number=False,  add_dummy_prefix=False)
spm.SentencePieceTrainer.train(input='ulm_test.txt', model_prefix='ulm_test',
                               vocab_size=13, split_by_number=False,  add_dummy_prefix=False)
# spm.SentencePieceTrainer.train(input='youku_continuous_none_tagged_tmp.txt', model_prefix='bpe_test',
#                                vocab_size=8000, split_by_number=False, add_dummy_prefix=False, model_type='bpe')
