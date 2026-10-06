const fs = require('node:fs');
const acorn = require('acorn');
const text = fs.readFileSync(0, 'utf8');
const tree = acorn.parse(text, { ecmaVersion: 'latest', locations: true });
const result = [];
function visit(node, parent, key, ancestors = []) {
  if (!node || typeof node !== 'object') return;
  if (node.type === 'Literal' && typeof node.value === 'string') {
    let technical = null;
    let display = false;
    for (const ancestor of ancestors) {
      if (ancestor.type === 'ForOfStatement'
        && node.start >= ancestor.right.start && node.end <= ancestor.right.end
        && text.slice(ancestor.body.start, ancestor.body.end).includes('getElementById')) {
        technical = 'DOM element id inventory';
      }
      if (ancestor.type !== 'CallExpression') continue;
      const name = ancestor.callee.type === 'Identifier' ? ancestor.callee.name : ancestor.callee.property?.name;
      const index = ancestor.arguments.findIndex(arg => node.start >= arg.start && node.end <= arg.end);
      if (name === 'el' && index >= 0 && index < 2 || name === 'span' && index === 0) technical = 'DOM identifier expression';
      if (name === 'span' && index === 1 || name === 'el' && index === 2 || name === 'button' && index === 1) display = true;
    }
    if (parent.type === 'BinaryExpression' && ['===', '!==', '==', '!='].includes(parent.operator)
      || parent.type === 'SwitchCase'
      || parent.type === 'Property' && key === 'key'
      || parent.type === 'ExpressionStatement' && parent.directive
      || parent.type === 'MemberExpression' && key === 'property') technical = 'JavaScript protocol, grammar or lookup token';
    if (parent.type === 'CallExpression') {
      const callee = parent.callee;
      const name = callee.type === 'Identifier' ? callee.name : callee.property?.name;
      const index = parent.arguments.indexOf(node);
      if (name === 'el' && index < 2 || name === 'span' && index === 0 || name === 'showModal' && index === 0
        || ['querySelector', 'querySelectorAll', 'getElementById', 'createElement', 'addEventListener', 'removeEventListener', 'fetch', 'setAttribute', 'getAttribute', 'matches', 'closest', 'toggle', 'add', 'remove', 'contains'].includes(name)) {
        technical = 'DOM, event, style or resource identifier';
      }
    }
    if (parent.type === 'Property' && key === 'value'
      && ['event', 'cache', 'kind', 'mode', 'type', 'marker', 'insert'].includes(parent.key.name)) technical = 'JavaScript protocol or editor token';
    if (parent.type === 'AssignmentExpression' && parent.left.type === 'MemberExpression'
      && ['className', 'type', 'id'].includes(parent.left.property.name)) technical = 'DOM identifier';
    result.push({ start: Array.from(text.slice(0, node.start)).length,
      end: Array.from(text.slice(0, node.end)).length, line: node.loc.start.line,
      technical, display,
      source: node.value, parent: parent.type, key,
      before: text.slice(Math.max(0, node.start - 90), node.start),
      after: text.slice(node.end, node.end + 40) });
  }
  if (node.type === 'TemplateLiteral') {
    throw new Error('Review new JavaScript template literals before publishing translations');
  }
  for (const [childKey, child] of Object.entries(node)) {
    if (Array.isArray(child)) child.forEach(value => visit(value, node, childKey, [...ancestors, node]));
    else if (child && typeof child === 'object') visit(child, node, childKey, [...ancestors, node]);
  }
}
visit(tree, null, '');
process.stdout.write(JSON.stringify(result));
