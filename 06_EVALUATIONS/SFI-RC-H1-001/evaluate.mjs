import { readFileSync, writeFileSync } from 'node:fs';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
const registry=JSON.parse(readFileSync(new URL('./claim_registry.json',import.meta.url),'utf8'));
const sourceById=new Map(registry.sources.map(source=>[source.id,source]));
assert.equal(sourceById.size,registry.sources.length,'source IDs must be unique');
assert.equal(new Set(registry.claims.map(claim=>claim.id)).size,registry.claims.length,'claim IDs must be unique');
for(const source of registry.sources){
 assert(/^\d{4}-\d{2}-\d{2}$/.test(source.published),'published date must be ISO');
 assert(source.url.startsWith('https://'),'public HTTPS source required');
}
for(const claim of registry.claims){
 assert(sourceById.has(claim.source),'claim source is required');
 assert(claim.locator && claim.state,'claim must declare locator and epistemic state');
}
const cuts=registry.cutoffs.map(cutoff=>{
 const eligible=registry.claims.filter(claim=>sourceById.get(claim.source).published<=cutoff).map(claim=>claim.id);
 const withheld=registry.claims.filter(claim=>sourceById.get(claim.source).published>cutoff).map(claim=>claim.id);
 assert.equal(eligible.length+withheld.length,registry.claims.length);
 return {cutoff,eligibleIds:eligible,withheldIds:withheld,eligibleCount:eligible.length,withheldCount:withheld.length,dateBlindNegativeControlWouldInclude:registry.claims.length};
});
assert.deepEqual(cuts.map(x=>x.eligibleCount),[3,7],'documentary historical cutoff invariant');
const result={contract:'SFI-RC-H1-001-RESULT-0.1',status:'DERIVED_SELF_TEST',h1ComparativeTrial:'NOT_TESTED',sources:registry.sources.length,claims:registry.claims.length,cuts,limits:['Hand-selected claim set, same author controls the instrument and outcome.','Counterfactual date-blind arm is an intentionally defective negative control, not an independently tested conventional workflow.','Source availability in selected set does not imply that other contemporaneous sources were unavailable.','No independent raters, randomization, source volume matching, time/cost equivalence, independent replication or external RETURN.','The documents are issuer statements/regulatory findings, not primary trading system logs.']};
writeFileSync(new URL('./results.json',import.meta.url),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({ok:true,claimRegistrySha256:createHash('sha256').update(readFileSync(new URL('./claim_registry.json',import.meta.url))).digest('hex'),result},null,2));