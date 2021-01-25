  ```cpp
  // Returns the score of `id`.
  // Score represents a log probability of the piece.
  // We can roughly estimate the unigram frequency of the piece.
  virtual float GetScore(int id) const {
    return model_proto_->pieces(id).score();
  }
  ```
  相加即可？Viterbi Algorithm？