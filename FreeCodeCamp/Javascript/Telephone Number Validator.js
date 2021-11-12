function telephoneCheck(str) {
  const checker = /^(\([0-9]{3}\)|[0-9]{3}-)[0-9]{3}-[0-9]{4}$|^1?\s?(\(\d{3}\)|\d{3})(\s|-)?\d{3}(\s|-)?\d{4}$/gm
  return checker.test(str);
}

telephoneCheck("555-555-5555");
